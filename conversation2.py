import re
import sys

import config
import constants
config.setup_examples()
import infermedica_api

api: infermedica_api.APIv3Connector = infermedica_api.get_api()

class AmbiguousAnswerException(Exception):
    pass

def read_input(prompt):
    """Displays appropriate prompt and reads the input.
    Args:
        prompt (str): String to be displayed.
    Returns:
        str: Stripped users input.
    """
    if prompt.endswith('?'):
        prompt = prompt + ' '
    else:
        prompt = prompt + ': '
    print(prompt, end='', flush=True)
    return sys.stdin.readline().strip()


def read_age_sex():
    """Reads age and sex specification such as "30 male".
    This is very crude. This is because reading answers to simple questions is
    not the main scope of this example. In real chatbots, either use some real
    intent+slot recogniser such as snips_nlu, or at least write a number of
    regular expressions to capture most typical patterns for a given language.
    Also, age below 12 should be rejected as our current knowledge doesn't
    support paediatrics (it's being developed but not delivered yet).
    Returns:
        int, str: Age and sex.
    """
    answer = read_input("Patient age and sex (e.g., 30 male)")
    try:
        age = int(extract_age(answer))
        sex = extract_sex(answer, constants.SEX_NORM)
        if age < constants.MIN_AGE:
            raise ValueError("Ages below 12 are not yet supported.")
        if age > constants.MAX_AGE:
            raise ValueError("Maximum possible age is 130.")
    except (AmbiguousAnswerException, ValueError) as e:
        print("{} Please repeat.".format(e))
        return read_age_sex()
    return age, sex

def extract_sex(text, mapping):
    """Extracts sex keywords from text.
    Args:
        text (str): Text from which the keywords will be extracted.
        mapping (dict): Mapping from keyword to sex.
    Returns:
        str: Single decision (one of `mapping` values).
    Raises:
        AmbiguousAnswerException: If `text` contains keywords mapping to two
            or more different distinct sexes.
        ValueError: If no keywords can be found in `text`.
    """
    sex_keywords = set(extract_keywords(text, mapping.keys()))
    if len(sex_keywords) == 1:
        return mapping[sex_keywords.pop().lower()]
    elif len(sex_keywords) > 1:
        raise AmbiguousAnswerException("I understood multiple sexes.")
    else:
        raise ValueError("No sex found.")


def extract_age(text):
    """Extracts age from text.
    Args:
        text (str): Text from which the keywords will be extracted.
    Returns:
        str: Found number (as a string).
    Raises:
        AmbiguousAnswerException: If `text` contains two or more numbers.
        ValueError: If no numbers can be found in `text`.
    """
    ages = set(re.findall(r"\b\d+\b", text))
    if len(ages) == 1:
        return ages.pop()
    elif len(ages) > 1:
        raise AmbiguousAnswerException("I understood multiple ages.")
    else:
        raise ValueError("No age found.")

def extract_keywords(text, keywords):
    """Extracts keywords from text.
    Args:
        text (str): Text from which the keywords will be extracted.
        keywords (list): Keywords to look for.
    Returns:
        list: All keywords found in text.
    """
    # Construct an alternative regex pattern for each keyword (speeds up the
    # search). Note that keywords must me escaped as they could potentialy
    # contain regex-specific symbols, e.g. ?, *.
    pattern = r"|".join(r"\b{}\b".format(re.escape(keyword))
                        for keyword in keywords)
    mentions_regex = re.compile(pattern, flags=re.I)
    return mentions_regex.findall(text)

def mentions_to_evidence(mentions):
    """Convert mentions (from /parse endpoint) to evidence structure as
    expected by the /diagnosis endpoint.
    """
    return [{'id': m['id'], 'choice_id': m['choice_id'], 'source': 'initial'}
            for m in mentions]