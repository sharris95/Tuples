#Formatting Flight Itineraries

def format_itineraries(itineraries):
    formatted_itineraries = []
    for i, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
        formatted_itineraries.append(f"Itinerary {i}: {traveler_name} - From {origin} to {destination}")
    return "\n".join(formatted_itineraries)

# Example usage:
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
print(format_itineraries(itineraries))