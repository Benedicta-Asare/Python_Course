#8-9. Messages

def show_messages(messages):
    for message in messages:
        print(message)

text_messages = ['hi', 'hello', 'sorry', 'goodbye']
show_messages(text_messages)


#8-10. Sending Messages

print("\n --- Sending Messages --- ")
def send_messages(sending, sent):
    while sending:
        message = sending.pop()
        print(message)
        sent.append(message)

text_messages = ['hi', 'hello', 'sorry', 'goodbye']
sent_messages = []
send_messages(text_messages, sent_messages)

print(f"\nUnsent = {text_messages}")
print(f"Sent = {sent_messages}\n")


#8-11. Archived Messages

def send_messages(sending, sent):
    while sending:
        message = sending.pop()
        print(message)
        sent.append(message)

text_messages = ['hi', 'hello', 'sorry', 'goodbye']
sent_messages = []
send_messages(text_messages[:], sent_messages)

print(f"\nUnsent = {text_messages}")
print(f"Sent = {sent_messages}")
