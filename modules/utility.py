from InquirerPy import inquirer

# GLOBAL VAR
page = 0


def long_rawlist(options: list):
    global page
    page = 0

    while True:
        list = options[7*page:7+7*page]
        if page > 0:
            list.append("Prev page")

        if (page+1)*7 < len(options):
            list.append("Next page")

        ans = inquirer.rawlist(
            message="What item would you like to search for:",
            default=2,
            choices=list
        ).execute()

        if ans == "Next page" and (page+1)*7 < len(options):
            page += 1
        elif ans == "Prev page" and page > 0:
            page -= 1
        else:
            return ans
