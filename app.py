print("Hello! Welcome to the AI-ChatBot.")
print("I am here to help answer your questions and make your experience easier!")

# Simple interaction
answer = input("Are you excited to interact with this chatbot? (yes/no) ").lower()

if answer == "yes":
    print("That's great! I'm excited to help you with any questions you have.")
elif answer == "no":
    print("No worries! I hope I can make your experience enjoyable and helpful.")
else:
    print("Hmm… I didn't quite understand that. Feel free to ask me any question!")

# FAQ dictionary
faq_dict = {
    "services": "I can help answer FAQs, assist customers, and provide quick responses to common questions.",
    "hours": "Our support team is available 24/7 to help you.",
    "pricing": "You can check our website for up-to-date pricing information.",
    "contact": "You can reach us via email at support@business.com.",
    "location": "Our office is located in Dubai, UAE, but we serve clients worldwide.",
    "refund": "Refunds are processed within 5–7 business days, depending on your bank.",
    "delivery": "Standard delivery takes 3–5 business days. Express delivery is also available.",
    "about": "We are a customer-focused company using AI to improve business efficiency.",
    "support": "You can reach our support team anytime via live chat or email.",
    "careers": "Visit our Careers page to explore open positions and internship opportunities."
}

# Loop so user can ask multiple questions
while True:
    user_question = input("\nAsk me a question (or type 'quit' to exit): ").lower()

    if user_question == "quit":
        print("Thank you for chatting with me. Have a great day!")
        break

    found = False
    for key in faq_dict:
        if key in user_question:
            print(faq_dict[key])
            found = True
            break

    if not found:
        print("I'm still learning. Thank you for your question!")
