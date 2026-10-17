
import re

input_file = "input.txt"
output_file = "emails.txt"

try:
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    emails = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    emails = list(dict.fromkeys(emails))

    with open(output_file, "w", encoding="utf-8") as file:
        for email in emails:
            file.write(email + "\n")

    print("Email extraction completed!")
    print("Emails found:", len(emails))
    print("Saved results to", output_file)

    for email in emails:
        print(email)

except FileNotFoundError:
    print("Error: input.txt was not found.")
