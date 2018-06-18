def analysis(file, user_id):
    import pandas as pd
    df = pd.read_json(file)
    s = df[df.user_id==user_id].minutes
    return s.count(), s.sum()
