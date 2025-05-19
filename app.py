from flask import Flask, render_template, request

app = Flask(__name__)

def single_digit(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

def count_digits(dob):
    all_digits = [int(ch) for ch in dob if ch.isdigit()]
    counts = {str(i): all_digits.count(i) for i in range(1, 10)}
    return counts

qualities = {
    "1": ["Introvert", "Communicative", "Introvert Talkative"],
    "2": ["Sensitive", "Bright", "Excellent"],
    "3": ["Creative", "Very Sensitive", "Over Imaginative"],
    "4": ["Stable", "Practical, Rich", "Hardworking"],
    "5": ["Caring", "Balanced", "Determined"],
    "6": ["Good Advisor", "Original", "High Tempered"],
    "7": ["Good Learner", "Spiritual", "Learn through loss"],
    "8": ["Knowledgeable", "Rich, Properties", "Materialistic"],
    "9": ["Intelligent", "Famous", "Very Famous, Givers"]
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    if request.method == "POST":
        gender = request.form["gender"]
        name = request.form["name"]
        dob = request.form["dob"]
        date, month, year = map(int, dob.split("-"))

        driver = single_digit(date)
        conductor = single_digit(date + month + year)

        birth_year = single_digit(year)
        if gender == "male":
            lucky = 11 - birth_year
        else:
            lucky = 11 + birth_year

        success_mindset = single_digit(date + month)

        counts = count_digits(f"{date}{month}{year}")
        trait_summary = {}
        for num, count in counts.items():
            if count > 0:
                if count == 1:
                    trait_summary[num] = qualities[num][0]
                elif count == 2:
                    trait_summary[num] = qualities[num][1]
                else:
                    trait_summary[num] = qualities[num][2]

        result = {
            "driver": driver,
            "conductor": conductor,
            "lucky": lucky,
            "success": success_mindset,
            "traits": trait_summary
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
