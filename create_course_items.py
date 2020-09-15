import numpy as np
import pandas as pd
import api_key

canvas = api_key.use_key
course = canvas.get_course(310310)

""" COURSE SETUP """

# TODO update course name here?
# course.update(course={'name': 'Geographic Information Systems II'})

# create assignment groups
assignment_groups = ['Assignments', 'Labs', 'Quizzes', 'Project']

# after doing this you'll have to go back in and delete one of the default
# groups that canvas requires (should be called 'Assignments')
for i in assignment_groups:
    course.create_assignment_group(name = i)

# get assignment groups as object to retrieve id
group_names = []
group_ids = []
groups = course.get_assignment_groups()

for group in groups:
    group_names.append(group.name)
    group_ids.append(group.id)

data = {'name' : group_names, 'id' : group_ids}
df = pd.DataFrame(data = data)

# create late policy
# NOTE this isn't working; maybe i don't have permissions for it?
course.update(late_policy = {"missing_submission_deduction_enabled": True,
                             "late_submission_deduction_enabled": True,
                             "late_submission_deduction": 20,
                             "late_submission_interval": "day"})

# TODO create discussion boards for each lab (done manually already)

""" ASSIGNMENTS """

due_dates_assignments = ["2020-09-09T23:59:00",
                         "2020-09-16T23:59:00",
                         "2020-09-23T23:59:00",
                         "2020-09-30T23:59:00",
                         "2020-10-07T23:59:00",
                         "2020-10-14T23:59:00",
                         "2020-10-21T23:59:00",
                         "2020-10-28T23:59:00",
                         "2020-11-04T23:59:00",
                         "2020-11-11T23:59:00",
                         "2020-11-18T23:59:00",
                         "2020-12-02T23:59:00",
                         "2020-12-09T23:59:00"]

# create assignment items and dropboxes
for i in range(len(due_dates_assignments)):
    course.create_assignment(assignment = {"name" : "Assignment {}".format(i+1),
                                           "submission_types" : "online_upload",
                                           "allowed_extensions" : "pdf",
                                           "turnitin_enabled" : True,
                                           "points_possible" : 100,
                                           "assignment_group_id" : int(df[df['name'] == 'Assignments']['id']),
                                           "due_at" : due_dates_assignments[i],
                                           "published" : True})

""" LABS """

due_dates_labs = ["2020-09-11T23:59:00",
                  "2020-09-18T23:59:00",
                  "2020-10-02T23:59:00",
                  "2020-10-09T23:59:00",
                  "2020-10-23T23:59:00",
                  "2020-11-06T23:59:00",
                  "2020-11-13T23:59:00",
                  "2020-11-20T23:59:00",
                  "2020-12-04T23:59:00"]

# create assignment items and dropboxes
for i in range(len(due_dates_labs)):
    course.create_assignment(assignment = {"name" : "Lab {}".format(i+1),
                                           "submission_types" : "online_upload",
                                           "allowed_extensions" : "pdf",
                                           "turnitin_enabled" : False,
                                           "points_possible" : 100,
                                           "assignment_group_id" : int(df[df['name'] == 'Labs']['id']),
                                           "due_at" : due_dates_labs[i],
                                           "published" : True})

""" Project """

due_dates_project = ["2020-09-25T23:59:00",
                     "2020-10-30T23:59:00",
                     "2020-12-16T23:59:00"]

# create assignment items and dropboxes
for i in range(len(due_dates_project)):
    course.create_assignment(assignment = {"name" : "Project part {}".format(i+1),
                                           "submission_types" : "online_upload",
                                           "allowed_extensions" : "pdf",
                                           "turnitin_enabled" : True,
                                           "points_possible" : 100,
                                           "assignment_group_id" : int(df[df['name'] == 'Project']['id']),
                                           "due_at" : due_dates_project[i],
                                           "published" : True})

""" Quizzes """

due_dates_quizzes = ["2020-10-16T23:59:00",
                     "2020-11-25T23:59:00"]

# create assignment items and dropboxes
for i in range(len(due_dates_quizzes)):
    course.create_assignment(assignment = {"name" : "Quiz {}".format(i+1),
                                           "points_possible" : 100,
                                           "assignment_group_id" : int(df[df['name'] == 'Quizzes']['id']),
                                           "due_at" : due_dates_quizzes[i],
                                           "published" : True})
