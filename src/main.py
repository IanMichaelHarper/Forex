from helpers.extract import GSheets

if __name__ == '__main__':
    sheet = GSheets()
    values = sheet.get_values()

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))
