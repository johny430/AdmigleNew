from google.ads.googleads.client import GoogleAdsClient

# scopes = ["https://www.googleapis.com/auth/adwords"]

# flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file="client_secret_534721407121-jqvsunp4t3s24m8nj5gv64ki392e8v7o.apps.googleusercontent.com.json",scopes=scopes)

# credentials = flow.run_local_server()

googleads_client = GoogleAdsClient.load_from_storage(path="googleads.yaml")


def main(client, customer_id):
    ga_service = client.get_service("GoogleAdsService")

    query = "SELECT customer.id FROM customer LIMIT 1"
    request = client.get_type("SearchGoogleAdsRequest")
    request.customer_id = customer_id
    request.query = query
    responce = ga_service.search(request=request)
    customer_id = list(responce)[0]
    print(customer_id)
    print(responce)
    # stream = ga_service.search_stream(customer_id=customer_id, query=query)
    #
    # for batch in stream:
    #     for row in batch.results:
    #         print(
    #             f"Campaign with ID {row.campaign.id} and name "
    #             f'"{row.campaign.name}" was found.'
    #         )


if __name__ == '__main__':
    main(client=googleads_client, customer_id="2627554345")
