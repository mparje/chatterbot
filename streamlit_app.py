import random
import streamlit as st
import matplotlib.pyplot as plt

# Define the Streamlit application
def main():
    # Set the page title and layout
    st.title("Floor Plan Generator")
    st.sidebar.title("Customization Options")
    st.sidebar.markdown("Adjust the settings to customize the floor plan.")

    # Add input fields for house dimensions
    st.subheader("House Dimensions")
    house_length = st.number_input("Length (in meters)", min_value=1, step=1)
    house_width = st.number_input("Width (in meters)", min_value=1, step=1)
    num_rooms = st.number_input("Number of Rooms", min_value=1, step=1)

    # Generate floor plan on button click
    if st.button("Generate Floor Plan"):
        # Call a function to generate the floor plan based on the provided dimensions
        floor_plan = generate_floor_plan(house_length, house_width, num_rooms)

        # Display the floor plan
        st.subheader("Floor Plan")
        st.pyplot(floor_plan)

# Function to generate the floor plan
def generate_floor_plan(length, width, num_rooms):
    # Create a figure and axis for the floor plan
    fig, ax = plt.subplots(figsize=(10, 6))

    # Set the axis limits based on the house dimensions
    ax.set_xlim(0, length)
    ax.set_ylim(0, width)

    # Draw the house boundary
    house_boundary = plt.Rectangle((0, 0), length, width, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(house_boundary)

    # Generate and position the rooms randomly
    for room_num in range(1, num_rooms+1):
        room_length = random.randint(1, length)
        room_width = random.randint(1, width)
        room_x = random.randint(0, length - room_length)
        room_y = random.randint(0, width - room_width)

        room = plt.Rectangle((room_x, room_y), room_length, room_width, fill=True, alpha=0.5)
        ax.add_patch(room)

        # Add room labels
        ax.text(room_x + room_length / 2, room_y + room_width / 2, f"Room {room_num}", ha='center', va='center')

    # Set axis labels and title
    ax.set_xlabel('Length (m)')
    ax.set_ylabel('Width (m)')
    ax.set_title('Floor Plan')

    # Remove the axis ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Adjust the layout
    plt.tight_layout()

    return fig

# Run the Streamlit application
if __name__ == "__main__":
    main()
