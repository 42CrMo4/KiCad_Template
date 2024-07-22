import re
import os

def parse_version(tag):
    match = re.match(r'v?(\d+)\.(\d+)\.(\d+)(?:-rc\.(\d+))?', tag)
    if match:
        return tuple(int(x) if x is not None else 0 for x in match.groups())
    return (0, 0, 0, 0)  # Return a default tuple for non-matching tags

with open('all_tags.txt', 'r') as f:
    tags = [line.strip() for line in f]

release_tags = [tag for tag in tags if 'rc' not in tag]
rc_tags = [tag for tag in tags if 'rc' in tag]

sorted_release_tags = sorted(release_tags, key=parse_version, reverse=True)
sorted_rc_tags = sorted(rc_tags, key=parse_version, reverse=True)

with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
    f.write(f"LAST_TAG={tags[0] if tags else 'None'}\n")
    f.write(f"LAST_RELEASE_TAG={sorted_release_tags[0] if sorted_release_tags else 'None'}\n")
    f.write(f"SECOND_LAST_RELEASE_TAG={sorted_release_tags[1] if len(sorted_release_tags) > 1 else 'None'}\n")
    f.write(f"LAST_RC_TAG={sorted_rc_tags[0] if sorted_rc_tags else 'None'}\n")
    f.write(f"SECOND_LAST_RC_TAG={sorted_rc_tags[1] if len(sorted_rc_tags) > 1 else 'None'}\n")

# Print debug information
print("All tags:", tags)
print("Release tags:", release_tags)
print("RC tags:", rc_tags)
print("Sorted release tags:", sorted_release_tags)
print("Sorted RC tags:", sorted_rc_tags)
