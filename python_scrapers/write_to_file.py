filename = "soup_output.html"
# Open the file in write mode (creating it if it doesn't exist)
with open(filename, "w", encoding="utf-8") as f:
    # Write the prettified version of the soup object to the file
    f.write(soup.prettify())
print("Output written to", filename)