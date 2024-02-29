from player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player in self.players:
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        try:
            p = next(filter(lambda x: x.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        self.players.remove(p)
        p.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."
        # for p in self.players:
        #     if p.name == player_name:
        #         p.guild = "Unaffiliated"
        #         self.players.remove(p)
        #         return f"Player {player_name} has been removed from the guild."
        # return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for curr_player in self.players:
            result += f"{curr_player.player_info()}\n"
        return result
