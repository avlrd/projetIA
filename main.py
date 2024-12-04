import picsellia as pc

organization_name = "Picsalex-MLOps"

client = pc.Client(api_token="185e119a0205ca1a92bf65af09c0469eecca2500", organization_name=organization_name)

dataset = client.get_dataset_by_id('01930b78-95d2-7ec5-9e09-3e2b00ee4af4')

print(dataset)

dataset_version = client.get_dataset_version_by_id('01930b78-9bed-7b90-943a-2e18da8726c5')

print(dataset_version)