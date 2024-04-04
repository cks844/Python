def print_reverse(sent):
    l = sent.split()
    new_sent = ""
    for i in l:
        new_sent = i +" "+new_sent
    return (new_sent)
sent = input("Enter the sentence:")
print_reverse(sent)
