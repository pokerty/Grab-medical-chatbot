import conversation

def run():
    age, sex = conversation.read_age_sex()
    print(f"OK, {age} year old {sex}.")
    age = {'value': age, 'unit':'year'}



if __name__ == "__main__":
    run()