class VehicleEntry(AssetEntry):
    def __init__(self, asset_id, asset_name, asset_type, asset_location, asset_condition, purchase_date, purchase_price, depreciation_rate, make, model, mileage):
        super().__init__(asset_id, asset_name, asset_type, asset_location, asset_condition, purchase_date, purchase_price, depreciation_rate)
        self.make = make
        self.model = model
        self.mileage = mileage

    def update_asset(self, attribute, new_value):
        if attribute == 'asset_condition':
            if self.asset_type == 'Car' and new_value not in ['Excellent', 'Good', 'Fair', 'Poor']:
                print("Invalid value for asset_condition for a car.")
            elif self.asset_type == 'Truck' and new_value not in ['Excellent', 'Good', 'Fair']:
                print("Invalid value for asset_condition for a truck.")
            else:
                self.asset_condition = new_value
        elif attribute == 'mileage':
            self.mileage = new_value
        else:
            super().update_asset(attribute, new_value)