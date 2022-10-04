# Description:
#
# Your task is to implement a function that calculates an election winner from a list of voter selections using an Instant Runoff Voting algorithm. If you haven't heard of IRV, here's a basic overview (slightly altered for this kata):
#
#     Each voter selects several candidates in order of preference.
#     The votes are tallied from the each voter's first choice.
#     If the first-place candidate has more than half the total votes, they win.
#     Otherwise, find the candidate who got the least votes and remove them from each person's voting list.
#     In case of a tie for least, remove all of the tying candidates.
#     In case of a complete tie between every candidate, return nil(Ruby)/None(Python)/undefined(JS).
#     Start over.
#     Continue until somebody has more than half the votes; they are the winner.
#
# Your function will be given a list of voter ballots; each ballot will be a list of candidates (symbols) in descending order of preference. You should return the symbol corresponding to the winning candidate. See the default test for an example!
#
# My solution:
def runoff(voters):
    while True:

        f_place = []
        for v in voters:
            f_place.append(v[0])

        # check if all candidates are in f_place list if not delete them from voters
        to_del = []
        for v in voters[0]:
            if v not in f_place:
                to_del.append(v)

        if to_del != []:
            for voter in voters:
                for candidate in to_del:
                    voter.remove(candidate)
        else:
            if len(set(f_place)) == 1:
                return f_place[0]

            votes = [[x, f_place.count(x)] for x in set(f_place)]
            votes = sorted(votes, key=lambda x: x[1], reverse=True)

            max_votes = votes[0][1]
            min_votes = votes[-1][1]

            if max_votes == min_votes:
                return None
            else:
                if max_votes > len(f_place) / 2:
                    return votes[0][0]
                else:
                    for voter in voters:
                        for vote in votes:
                            if vote[1] == min_votes:
                                voter.remove(vote[0])
            if voters == []:
                return None
            if len(voters[0]) == 1:
                return voters[0][0]