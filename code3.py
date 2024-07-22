import re
import os

def parse_version(tag):
    match = re.match(r'v(\d+)\.(\d+)(?:-rc(\d+))?$', tag)
    if match:
        return tuple(int(x) if x is not None else 0 for x in match.groups())
    return None

def debug_print(message):
    print(f"DEBUG: {message}")

# Get the triggering tag from GITHUB_REF
trigger_tag = "diff"
debug_print(f"Trigger tag: {trigger_tag}")

# Get all tags and sort them
all_tags = [tag.strip() for tag in os.popen('git tag -l').readlines()]
debug_print(f"All tags: {all_tags}")

sorted_tags = sorted(all_tags, key=lambda t: parse_version(t) or (0, 0, 0), reverse=True)
debug_print(f"Sorted tags: {sorted_tags}")

trigger_version = parse_version(trigger_tag)
debug_print(f"Parsed trigger version: {trigger_version}")

# Separate RC and release tags
rc_tags = [tag for tag in sorted_tags if parse_version(tag) and parse_version(tag)[2] != 0]
release_tags = [tag for tag in sorted_tags if parse_version(tag) and parse_version(tag)[2] == 0]

if trigger_version:
    release_base = f"v{trigger_version[0]}.{trigger_version[1]}"
    is_rc = trigger_version[2] != 0
    debug_print(f"Is RC: {is_rc}")

    if is_rc:
        # For RC tags
        previous_rc = next((tag for tag in sorted_tags 
                            if tag.startswith(f"{release_base}-rc") 
                            and parse_version(tag) < trigger_version), None)
        previous_release = next((tag for tag in release_tags 
                                if parse_version(tag) < trigger_version), None)
    else:
        # For release tags
        previous_rc = next((tag for tag in sorted_tags if tag.startswith(f"{release_base}-rc")), None)
        previous_release = next((tag for tag in release_tags 
                                if parse_version(tag) < trigger_version), None)
else:
    debug_print("Unrecognized tag format. Using fallback logic.")
    previous_rc = rc_tags[0] if rc_tags else None
    previous_release = release_tags[0] if release_tags else None
    is_rc = False

debug_print(f"Previous RC: {previous_rc}")
debug_print(f"Previous Release: {previous_release}")

with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
    f.write(f"TRIGGER_TAG={trigger_tag}\n")
    f.write(f"IS_RC={'true' if is_rc else 'false'}\n")
    f.write(f"PREVIOUS_RC={previous_rc or 'None'}\n")
    f.write(f"PREVIOUS_RELEASE={previous_release or 'None'}\n")
    if not trigger_version:
        f.write("UNRECOGNIZED_TAG=true\n")

debug_print("Tag analysis complete")