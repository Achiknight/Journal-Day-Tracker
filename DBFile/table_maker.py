
class qurreys():
    def create_row_sleep(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "sleep" TEXT')
        data.commit()

    def create_row_steps(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "steps" TEXT')
        data.commit()

    def create_row_water(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "water" TEXT')
        data.commit()

    def create_row_study(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "study" TEXT')
        data.commit()

    def create_row_coding(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "coding" TEXT')
        data.commit()

    def create_row_gaming(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "gaming" TEXT')
        data.commit()

    def create_row_screen_time(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "screen_time" TEXT')
        data.commit()

    def create_row_exercise(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "exercise" TEXT')
        data.commit()

    def create_row_caffeine(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "caffeine" TEXT')
        data.commit()

    def create_row_spent_today(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "spent_today" TEXT')
        data.commit()

    def create_row_mood(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "mood" INTEGER')
        data.commit()

    def create_row_energy(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "energy" INTEGER')
        data.commit()

    def create_row_stress(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "stress" INTEGER')
        data.commit()

    def create_row_productivity(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "productivity" INTEGER')
        data.commit()

    def create_row_weather(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "weather" TEXT')
        data.commit()

    def create_row_temperature(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "temperature" TEXT')
        data.commit()

    def create_row_classes_attended(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "classes_attended" TEXT')
        data.commit()

    def create_row_attendance(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "attendance" TEXT')
        data.commit()

    def create_row_assignments_completed(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "assignments_completed" TEXT')
        data.commit()

    def create_row_new_people_met(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "new_people_met" TEXT')
        data.commit()

    def create_row_interesting_thing_learned(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "interesting_thing_learned" TEXT')
        data.commit()

    def create_row_best_moment(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "best_moment" TEXT')
        data.commit()

    def create_row_most_chaotic_moment(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "most_chaotic_moment" TEXT')
        data.commit()

    def create_row_git_commits(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "git_commits" TEXT')
        data.commit()

    def create_row_coding_time(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "coding_time" TEXT')
        data.commit()

    def create_row_bugs_fixed(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "bugs_fixed" TEXT')
        data.commit()

    def create_row_features_added(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "features_added" TEXT')
        data.commit()

    def create_row_what_i_learned(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "what_i_learned" TEXT')
        data.commit()

    def create_row_current_project(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "current_project" TEXT')
        data.commit()

    def create_row_music_listening(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "music_listening" TEXT')
        data.commit()

    def create_row_current_song(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "current_song" TEXT')
        data.commit()

    def create_row_movies_episodes(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "movies_episodes" TEXT')
        data.commit()

    def create_row_games_played(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "games_played" TEXT')
        data.commit()

    def create_row_gaming_time(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "gaming_time" TEXT')
        data.commit()

    def create_row_starting_balance(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "starting_balance" TEXT')
        data.commit()

    def create_row_spent(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "spent" TEXT')
        data.commit()

    def create_row_food(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "food" TEXT')
        data.commit()

    def create_row_transport(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "transport" TEXT')
        data.commit()

    def create_row_entertainment(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "entertainment" TEXT')
        data.commit()

    def create_row_saved(cur, data, journal_name):
        cur.execute(f'ALTER TABLE "journal_{journal_name}" ADD COLUMN "saved" TEXT')
        data.commit()


    create_row_functions = {
        "Sleep": create_row_sleep,
        "Steps": create_row_steps,
        "Water": create_row_water,
        "Study": create_row_study,
        "Coding": create_row_coding,
        "Gaming": create_row_gaming,
        "Screen Time": create_row_screen_time,
        "Exercise": create_row_exercise,
        "Caffeine": create_row_caffeine,
        "Spent Today": create_row_spent_today,
        "Mood": create_row_mood,
        "Energy": create_row_energy,
        "Stress": create_row_stress,
        "Productivity": create_row_productivity,
        "Weather": create_row_weather,
        "Temperature": create_row_temperature,
        "Classes Attended": create_row_classes_attended,
        "Attendance": create_row_attendance,
        "Assignments Completed": create_row_assignments_completed,
        "New People Met": create_row_new_people_met,
        "Interesting Thing Learned": create_row_interesting_thing_learned,
        "Best Moment": create_row_best_moment,
        "Most Chaotic Moment": create_row_most_chaotic_moment,
        "Git Commits": create_row_git_commits,
        "Coding Time": create_row_coding_time,
        "Bugs Fixed": create_row_bugs_fixed,
        "Features Added": create_row_features_added,
        "What I Learned": create_row_what_i_learned,
        "Current Project": create_row_current_project,
        "Music Listening": create_row_music_listening,
        "Current Song": create_row_current_song,
        "Movies/Episodes": create_row_movies_episodes,
        "Games Played": create_row_games_played,
        "Gaming Time": create_row_gaming_time,
        "Starting Balance": create_row_starting_balance,
        "Spent": create_row_spent,
        "Food": create_row_food,
        "Transport": create_row_transport,
        "Entertainment": create_row_entertainment,
        "Saved": create_row_saved,
    }