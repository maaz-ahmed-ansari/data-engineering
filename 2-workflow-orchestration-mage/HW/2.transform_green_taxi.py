if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    print(f"Preprocessing - rows with zero passengers: { data['passenger_count'].isin([0]).sum() }")

    print(f"Preprocessing - rows with trip_distance = 0: { data['trip_distance'].isin([0]).sum() }")

    # Remove rows where the passenger count is equal to 0 and the trip distance is equal to zero
    filtered_data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date
    filtered_data['lpep_pickup_date'] = filtered_data['lpep_pickup_datetime'].dt.date

    # Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id
    filtered_data.columns = (
        filtered_data.columns
        .str.replace(' ', '_')
        .str.lower()
    )

    return filtered_data


# Add three assertions:
# vendor_id is one of the existing values in the column (currently)
# passenger_count is greater than 0
# trip_distance is greater than 0

@test
def test_output(output, *args) -> None:

    assert 'vendorid' in output.columns, "'vendorid' column does not exist in the DataFrame."

@test
def test_output(output, *args) -> None:

    assert output['passenger_count'].isin([0]).sum() is not None, 'There are rides with zero passengers'

@test
def test_output(output, *args) -> None:

    assert output['trip_distance'].isin([0]).sum() is not None, 'There are rides with trip distance = 0'
