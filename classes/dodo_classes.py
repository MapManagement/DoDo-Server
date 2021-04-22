

class ToDoTask:

    def __init__(self, t_id, creator_id, text, color, creation_date, is_done):
        self.t_id = t_id
        self.creator_id = creator_id
        self.text = text
        self.color = color
        self.creation_date = creation_date
        self.is_done = is_done


class Note:

    def __init__(self, n_id, creator_id, title, text, color, creation_id, is_visible, is_highlighted):
        self.n_id = n_id
        self.creator_id = creator_id
        self.title = title
        self.text = text
        self.color = color
        self.creation_id = creation_id
        self.is_visible = is_visible
        self.is_highlighted = is_highlighted


class Profile:

    def __init__(self, p_id, name, creation_date):
        self.p_id = p_id
        self.name = name
        self.creation_date = creation_date


class Tag:

    def __init__(self, t_id, name):
        self.t_id = t_id
        self.name = name
