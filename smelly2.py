def get_percentage_visualisation(percentage):
  filled_blobs = int(percentage * 10)
  return ("●" * filled_blobs + "○" * (10-filled_blobs))


for i in range(0,11):
    print(f"{i/10} = {get_percentage_visualisation(i/10)}")
