                                             # PYTHON
# def greet_user(): 
#        name = input("Enter You Name: ")
#        print("Hello", name)

# greet_user()


# def greet_user():
#     try:
#         name = input('Enter your name: ')
#         print("Hello", name)
#     except:
#         print("Something Wrong!")

#     greet_user()    


                             #   JSON
    
# import json 

# data = '{ "name" : "Naila", "age" : 25}'

# parased_data = json.loads(data)

# print(parased_data["name"])
# print(parased_data["age"])
# # print(type(data))
# # print(type(parased_data))


                              # API CALLS

# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# data = response.json()
# print(data["id"])
# print(data["title"])



# import requests

# def summarize_text():
#     url = "https://openrouter.ai/api/v1/chat/completions"

#     headers = {
#         "Authorization": "Bearer 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",
#         "Content-Type": "application/json"
#     }

#     user_input = input("Enter text to summarize: ")

#     data = {
#         "model": "openai/gpt-3.5-turbo",
#         "messages": [
#             {"role": "user", "content": f"Summarize this: {user_input}"}
#         ]
#     }

#     try:
#         response = requests.post(url, headers=headers, json=data)
#         result = response.json()

#         if "choices" in result:
#             summary = result["choices"][0]["message"]["content"]

#             print("\nSummary:\n")
#             print(summary)

#             # Save to file
#             with open("summary.txt", "w") as file:
#                 file.write(summary)

#         else:
#             print("Error from API:")
#             print(result)

#     except Exception as e:
#         print("Something went wrong:", e)


# summarize_text()




import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

api_key = os.getenv("API_KEY")


def summarize_text():
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    while True:
        

        user_input = input("\nEnter text to summarize (or type 'exit'): ")

        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break
        

       data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": f"Summarize this clearly in 2-3 complete sentences: {user_input}"}
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            # print(api_key)

            if "choices" in result:
                summary = result["choices"][0]["message"]["content"]

                print("\nSummary:\n")
                print(summary)

                with open("summary.txt", "a") as file:
                    file.write(summary + "\n\n")

            else:
                print("Error:", result)

        except Exception as e:
            print("Something went wrong:", e)



summarize_text()
