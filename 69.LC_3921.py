class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0
        for k in events:
            if counter == 10:
                break
            if k == "W":
                counter += 1
            elif k == "WD" or k == "NB":
                score += 1
            if k in "012346":
                score += int(k)
        return [score, counter]
