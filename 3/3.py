# import sys
# from argparse import ArgumentParser
# from typing import List, Optional

# from cvat_sdk import make_client
# from cvat_sdk.core.proxies.jobs import Job
# from cvat_sdk.core.helpers import get_paginated_collection
# from tqdm import tqdm


# def main(args: Optional[List[str]] = None) -> int:
#     parser = ArgumentParser()
#     parser.add_argument("project_id", type=int)
#     parsed_args = parser.parse_args(args)

#     with make_client("https://app.cvat.ai", port=443, credentials=('username', 'pass')) as client:
#         # client.organization_slug = ""
#         client.config.status_check_period = 2

#         all_annotations_count = {}

#         jobs = [
#             Job(client, job_model)
#             for job_model in  get_paginated_collection(
#                 client.jobs.api.list_endpoint, project_id=parsed_args.project_id
#             )
#         ]

#         for job in tqdm(jobs):
#             annotations = job.get_annotations()

#             annotations_count = {}
#             annotations_count["tag"] = annotations_count.get("tag", 0) + len(annotations.tags)
#             annotations_count["shapes"] = annotations_count.get("shapes", 0) + len(
#                 annotations.shapes
#             )
#             annotations_count["tracks"] = annotations_count.get("tracks", 0) + len(
#                 annotations.tracks
#             )

#             for shape in annotations.shapes:
#                 annotations_count[shape.type.value] = annotations_count.get(shape.type.value, 0) + 1

#             print(f"Job {job.id} counts:", annotations_count)

#             for k, v in annotations_count.items():
#                 all_annotations_count[k] = all_annotations_count.get(k, 0) + v

#         print("checked jobs", [j.id for j in jobs])
#         print("annotations count:", all_annotations_count)

#     return 0


# if __name__ == "__main__":
#     sys.exit(main(sys.argv[1:]))









import sys
from argparse import ArgumentParser
from typing import List, Optional
from cvat_sdk import make_client
from cvat_sdk.core.proxies.jobs import Job
from cvat_sdk.core.helpers import get_paginated_collection
from tqdm import tqdm

def main(args: Optional[List[str]] = None) -> int:
    parser = ArgumentParser()
    parser.add_argument("project_id", type=int)
    parsed_args = parser.parse_args(args)

    with make_client("https://app.cvat.ai", port=443, credentials=("username", "pass")) as client:
        jobs = [Job(client, job_model) for job_model in get_paginated_collection(client.jobs.api.list_endpoint, project_id=parsed_args.project_id)]

        all_annotations_count = {}
        for job in tqdm(jobs):
            annotations = job.get_annotations()
            annotations_count = {
                "tag": len(annotations.tags),
                "shapes": len(annotations.shapes),
                "tracks": len(annotations.tracks)
            }
            for shape in annotations.shapes:
                annotations_count[shape.type.value] = annotations_count.get(shape.type.value, 0) + 1

            print(f"Job {job.id} counts:", annotations_count)

            for k, v in annotations_count.items():
                all_annotations_count[k] = all_annotations_count.get(k, 0) + v

        print("Annotations count:", all_annotations_count)
        return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
