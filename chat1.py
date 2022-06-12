import conversation
import infermedica_api
import config
config.setup_examples()

api: infermedica_api.APIv3Connector = infermedica_api.get_api()

def receive(text, age, sex, symptom):
    # try:
    # print(age)
    if age==None and sex==None:
        read = conversation.read_age_sex(text)
        if read == "Please enter your age AND gender :)":
            # print("a")
            return (read, 0)
        else:  
            age, sex = read
            return (("What are your conditions?"), read)
    # print(f"OK, {age} year old {sex}.")
    age = {'value': age, 'unit':'year'}
    return run(age, sex, symptom)
    # except Exception as e:
    #     return "Please enter your age or gender :)"
        
    # if "diagnose" in text: 
    # return run(age, sex)


def run(age, sex, symptom):
    # choice = input("Which function do you want ?")
    #Remove the if this is an essential step 
    #If else statements are used to reduce the number of API calls
    #and length of programme during testing
    # if (choice == "parse"):
    # if symptom:
    # symptom = input("How are you feeling today ?")
    response = api.parse(symptom, age=age.get('value'))
    # print(response, end="\n\n")
    id = response.get('mentions',[]) #this returns a list need to figure out how to change to dictionary with just the id and choice_id
    print(id)
    #evidence is to be like the one in readme.md
    evidence = conversation.mentions_to_evidence(id)
    info = {
        "sex": sex,
        "age": age.get("value"),
        "evidence": evidence,
        "extras": {
            'disable_groups': True
        }
    }
    response1 = api.triage(**info)
    response2 = api.suggest(**info)
    fresponse = ""
    for item in response1:
        line="Your "+str(item)+" is "+str(response1[item])+".\n"
        fresponse+=line
    fresponse+="You could be down with "
    for item in response2:
        line=str(item['name'])+"/"+str(item['common_name'])+", "
        fresponse+=line
    return fresponse



if __name__ == "__main__":
    run()