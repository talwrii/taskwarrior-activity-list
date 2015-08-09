# taskwarrior activity list

An extension to taskwarrior which stores the details of when
you start and stop activities in annotations.

Provides a utility `twdisplay.py` to output summaries of
activities

# Usage

- Ensure you have a taskwarrior with version 2.4 or more recent
- Attach the hook

        ln -sf full_path_to/hook.py ~/.task/hooks/on_modify.tal

- Run the twdisplay utility to summarise output
        twdisplay.py --format csv [filter]

- Add things to your path as appropriate

# Caveats

- This probably hits up against performance issues at some point: the cost of starting and stopping a task is linear in the number of times it has started and stopped
- You might consider the extra noise in task info distracting

# Alternatives

- There is a similar project that writes into `timebook`
- Also another that keeps aggregates about the total time you have spent on projects
- `timetrap` and `timebook` are alternatives to taskwarrior which focus more on this type of logging. However I have found their insistence of a "current activity" a little problematic.
