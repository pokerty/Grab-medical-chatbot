import conversation2
import infermedica_api
import config
config.setup_examples()

api: infermedica_api.APIv3Connector = infermedica_api.get_api()

def run():
    age, sex = conversation2.read_age_sex()
    print(f"OK, {age} year old {sex}.")

    choice = input("Which function do you want ?")
    #Remove the if this is an essential step 
    #If else statements are used to reduce the number of API calls
    #and length of programme during testing
    if (choice == "parse"):
        symptom = input("How are you feeling today ?")
        response = api.parse(symptom, age = age)
        print(response, end="\n\n")
        id = response.get('mentions',[]) #this returns a list need to figure out how to change to dictionary with just the id and choice_id
        print(id)
        #evidence is to be like the one in readme.md
        evidence = conversation2.mentions_to_evidence(id)
        info = {
            "sex": sex,
            "age": age,
            "evidence": evidence,
            "extras": {
                'disable_groups': True
            }
        }

        print("\n\n", evidence)
        response = api.triage(**info)
        print("\n\n", response)
        response = api.suggest(**info)
        print("\n\n", response)



if __name__ == "__main__":
    run()