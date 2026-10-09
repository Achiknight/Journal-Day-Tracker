from customtkinter import *
from utility.Wid_Snip import *
from Backend.config import fg


class Journal_Widgets():



    #*      Dayily Stats

    def build_sleep(row):
        LabelBody(row, text="Sleep").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Hours slept")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_steps(row):
        LabelBody(row, text="Steps").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Step count")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_water(row):
        LabelBody(row, text="Water").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Glasses / litres")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_study(row):
        LabelBody(row, text="Study").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Hours studied")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_coding(row):
        LabelBody(row, text="Coding").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Hours coded")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_gaming(row):
        LabelBody(row, text="Gaming").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Hours gaming")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_screen_time(row):
        LabelBody(row, text="Screen Time").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Hours on screen")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_exercise(row):
        LabelBody(row, text="Exercise").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="What did you do?")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_caffeine(row):
        LabelBody(row, text="Caffeine").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Cups of coffee / tea")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_spent_today(row):
        LabelBody(row, text="Spent Today").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Amount spent")
        entry.pack(side="right", fill="x", expand=True)
        return entry


    #*          Daily Stats

    def build_mood(row):
        LabelBody(row, text="Mood").pack(side="left", padx=(0, 20))
        slider = CTkSlider(row, from_=1, to=10, number_of_steps=9)
        slider.set(5)
        slider.pack(side="right", fill="x", expand=True)
        return slider

    def build_energy(row):
        LabelBody(row, text="Energy").pack(side="left", padx=(0, 20))
        slider = CTkSlider(row, from_=1, to=10, number_of_steps=9)
        slider.set(5)
        slider.pack(side="right", fill="x", expand=True)
        return slider

    def build_stress(row):
        LabelBody(row, text="Stress").pack(side="left", padx=(0, 20))
        slider = CTkSlider(row, from_=1, to=10, number_of_steps=9)
        slider.set(5)
        slider.pack(side="right", fill="x", expand=True)
        return slider

    def build_productivity(row):
        LabelBody(row, text="Productivity").pack(side="left", padx=(0, 20))
        slider = CTkSlider(row, from_=1, to=10, number_of_steps=9)
        slider.set(5)
        slider.pack(side="right", fill="x", expand=True)
        return slider

    def build_weather(row):
        LabelBody(row, text="Weather").pack(side="left", padx=(0, 20))
        menu = CTkOptionMenu(row,
                            values=["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy", "Windy", "Foggy"],
                            fg_color=fg, button_color=fg)
        menu.pack(side="right")
        return menu

    def build_temperature(row):
        LabelBody(row, text="Temperature").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Temperature (°C)")
        entry.pack(side="right", fill="x", expand=True)
        return entry


    #*          Daily Stats

    def build_classes_attended(row):
        LabelBody(row, text="Classes Attended").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="How many classes")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_attendance(row):
        LabelBody(row, text="Attendance").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Attendance %")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_assignments_completed(row):
        LabelBody(row, text="Assignments Completed").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="How many assignments")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_new_people_met(row):
        LabelBody(row, text="New People Met").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Names or count")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_interesting_thing_learned(row):
        LabelBody(row, text="Interesting Thing Learned").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="What did you learn?")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_best_moment(row):
        LabelBody(row, text="Best Moment").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Best moment today")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_most_chaotic_moment(row):
        LabelBody(row, text="Most Chaotic Moment").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Most chaotic moment")
        entry.pack(side="right", fill="x", expand=True)
        return entry


    #*          Daily Stats

    def build_git_commits(row):
        LabelBody(row, text="Git Commits").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Number of commits")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_coding_time(row):
        LabelBody(row, text="Coding Time").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Hours coded")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_bugs_fixed(row):
        LabelBody(row, text="Bugs Fixed").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Number of bugs")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_features_added(row):
        LabelBody(row, text="Features Added").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Number of features")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_what_i_learned(row):
        LabelBody(row, text="What I Learned").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="What did you learn?")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_current_project(row):
        LabelBody(row, text="Current Project").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Project name")
        entry.pack(side="right", fill="x", expand=True)
        return entry


    #*          Daily stats

    def build_music_listening(row):
        LabelBody(row, text="Music Listening").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Hours of music")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_current_song(row):
        LabelBody(row, text="Current Song").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Song title")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_movies_episodes(row):
        LabelBody(row, text="Movies/Episodes").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Titles watched")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_games_played(row):
        LabelBody(row, text="Games Played").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Games played")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_gaming_time(row):
        LabelBody(row, text="Gaming Time").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Hours gaming")
        entry.pack(side="right", fill="x", expand=True)
        return entry


    #*          MONEY

    def build_starting_balance(row):
        LabelBody(row, text="Starting Balance").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Balance at start")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_spent(row):
        LabelBody(row, text="Spent").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Total spent")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_food(row):
        LabelBody(row, text="Food").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Food spending")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_transport(row):
        LabelBody(row, text="Transport").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Transport spending")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_entertainment(row):
        LabelBody(row, text="Entertainment").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Entertainment spending")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def build_saved(row):
        LabelBody(row, text="Saved").pack(side="left", padx=(0, 20))
        entry = Entery(row, placeholder_text="Amount saved")
        entry.pack(side="right", fill="x", expand=True)
        return entry



    FIELD_BUILDERS = {
        "Sleep": build_sleep,
        "Steps": build_steps,
        "Water": build_water,
        "Study": build_study,
        "Coding": build_coding,
        "Gaming": build_gaming,
        "Screen Time": build_screen_time,
        "Exercise": build_exercise,
        "Caffeine": build_caffeine,
        "Spent Today": build_spent_today,
        "Mood": build_mood,
        "Energy": build_energy,
        "Stress": build_stress,
        "Productivity": build_productivity,
        "Weather": build_weather,
        "Temperature": build_temperature,
        "Classes Attended": build_classes_attended,
        "Attendance": build_attendance,
        "Assignments Completed": build_assignments_completed,
        "New People Met": build_new_people_met,
        "Interesting Thing Learned": build_interesting_thing_learned,
        "Best Moment": build_best_moment,
        "Most Chaotic Moment": build_most_chaotic_moment,
        "Git Commits": build_git_commits,
        "Coding Time": build_coding_time,
        "Bugs Fixed": build_bugs_fixed,
        "Features Added": build_features_added,
        "What I Learned": build_what_i_learned,
        "Current Project": build_current_project,
        "Music Listening": build_music_listening,
        "Current Song": build_current_song,
        "Movies/Episodes": build_movies_episodes,
        "Games Played": build_games_played,
        "Gaming Time": build_gaming_time,
        "Starting Balance": build_starting_balance,
        "Spent": build_spent,
        "Food": build_food,
        "Transport": build_transport,
        "Entertainment": build_entertainment,
        "Saved": build_saved,
    }


