def calculate_total_time(number_of_photos, exposure_time):
    """
    Calculate the total time required to take a given number of photos,
    each with a specified exposure time.

    Parameters:
    - number_of_photos (int): The total number of photos to be taken.
    - exposure_time (float): The exposure time for each photo in seconds.

    Returns:
    - total_time (float): The total time required in seconds.
    """
    total_time = number_of_photos * exposure_time
    return total_time

# Input for the number of photos and exposure time
number_of_photos = int(input("Enter the number of photos: "))
exposure_time = float(input("Enter the exposure time for each photo (in seconds): "))

# Calculate and display the total time
total_time = calculate_total_time(number_of_photos, exposure_time)

# Convert total_time to hours, minutes, and seconds
hours = int(total_time // 3600)
minutes = int((total_time % 3600) // 60)
seconds = int(total_time % 60)

print(f"The total time required to take {number_of_photos} photos with an exposure time of {exposure_time} seconds each is {hours} hours, {minutes} minutes, and {seconds} seconds.")
