import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def main():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(
                spreadsheetId="1nEag84LaTqSv_OjYCGRY7WfKVeiOTzIjnmmlE5f0WCI",
                range="engenharia_de_software!A1:H27",
            )
            .execute()
        )
        values = result["values"]
        average = []
        situation = []
        absences = []
        naf_value = []
        total_naf = []

        for i, list in enumerate(values):  # Calculate and append the average in a list
            if i > 2:
                result = 0.0
                for j, list in enumerate(list):
                    if (j > 2 and j < 6):
                        result += float(values[i][j])
                result = result / 3 
                average.append(round(result))

        for i, list in enumerate(values):  # Get absences values and put them on a list
            if i > 2:
                absences_value = list[2]
                result = float(absences_value)
                absences.append(result)

        for i, average_value in enumerate(average):   # Get the average value and depending of the results, you're aprroved or not
            absences_value = absences[i]  
            if absences_value > 15:
                situation.append(["Reprovado por Falta"])
                result = 0  # On conditionals, the result gets 0 to facility calculum of naf's list
                naf_value.append(result)
            elif average_value > 70:
                situation.append(["Aprovado"])
                result = 0
                naf_value.append(result)
            elif average_value < 50:
                situation.append(["Reprovado por Nota"])
                result = 0
                naf_value.append(result)
            else:
                situation.append(["Exame Final"])
                result = average[i]
                naf_value.append(result)
        
        for naf in naf_value:  # Put naf on the sheet, together with the naf calculum
            if naf == 0:
                result = "0"
                total_naf.append([result])
            else:
                result = str(naf - 10)
                total_naf.append([result])


        result = (  # Uppdate the naf collumn
            sheet.values()
            .update(
                spreadsheetId="1nEag84LaTqSv_OjYCGRY7WfKVeiOTzIjnmmlE5f0WCI",
                range="engenharia_de_software!H4:H27",
                valueInputOption="RAW",
                body={"values": total_naf},
            )
            .execute()
        )
        
       
        result = (  # Update the situation collumn
            sheet.values()
            .update(
                spreadsheetId="1nEag84LaTqSv_OjYCGRY7WfKVeiOTzIjnmmlE5f0WCI",
                range="engenharia_de_software!G4:G27",
                valueInputOption="RAW",
                body={"values": situation},
            )
            .execute()
        )
    except HttpError as err:
        print(err)

if __name__ == "__main__":
    main()