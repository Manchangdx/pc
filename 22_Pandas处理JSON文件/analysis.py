def analysis(file, user_id):
    import pandas as pd
    df = pd.read_json(file)
    if user_id in list(df.user_id):
        s = df[df.user_id==user_id].minutes
        return s.count(), s.sum()
    return 0, 0
