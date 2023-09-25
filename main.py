from import_data import parse_data, highest_score

def main():
    #read CSV data from a plain-text file
    try:
        with open('TestData.csv', 'r') as file:
            csv_data = file.read()
    except Exception:
        print('file is not found')

    #parsing csv data from the string
    parsed_data = parse_data(csv_data)

    #calculate the highest score and names
    top_score, highest_score_names = highest_score(parsed_data)
    print("Name(s):")
    print('\n'.join(highest_score_names))
    print(f"Score: {top_score}")

if __name__ == "__main__":
    main()