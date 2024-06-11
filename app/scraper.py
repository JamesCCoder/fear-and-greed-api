import fear_and_greed

def get_fear_and_greed_index():
    try:
        index_data = fear_and_greed.get()
        return {"index_value": index_data.value, "status": index_data.description, "last_update": index_data.last_update}
    except Exception as e:
        print(f"Failed to fetch data: {e}")
        return None
