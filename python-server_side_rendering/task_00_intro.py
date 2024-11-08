import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return

    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries")
        return

    if not template.strip():
        print("Template is empty, no output files generated")
        return

    if not attendees:
        print("No data provided, no output files generated")
        return

    for idx, attendee in enumerate(attendees, start=1):
        invitation = template
        invitation = invitation.replace("{name}", attendee.get("name", "N/A"))
        invitation = invitation.replace(
            "{event_title}", attendee.get("event_title", "N/A"))
        invitation = invitation.replace(
            "{event_date}", attendee.get("event_date", "N/A"))
        invitation = invitation.replace(
            "{event_location}", attendee.get("event_location", "N/A"))

        output_filename = f"output_{idx}.txt"

        if os.path.exists("output"):
            print(f"Warning: Output file already exists and will be overwritten")

        try:
            with open(output_filename, "w") as file:
                file.write(invitation)
                print(
                    f"Generated invitation for {attendee['name']} saved to {output_filename}")
        except Exception as e:
            print(
                f"Error generating invitation for {attendee['name']}: {str(e)}")
