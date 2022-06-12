import conversation
import infermedica_api
import config

api: infermedica_api.APIv3Connector = infermedica_api.get_api()

def run():
    age, sex = conversation.read_age_sex()
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
        evidence = conversation.mentions_to_evidence(id)
        print("\n\n", evidence)
        response = api.suggest(**evidence)
        print("\n\n", response)



if __name__ == "__main__":
    run()