import pandas as pd

if __name__ == '__main__':
    # 我只是想看一下iloc和loc的源码
    df = pd.DataFrame({
          'A': [1, 2]
        , 'B': pd.Categorical(['zhangsan', 'lisi'])
        , 'C': pd.Categorical(['yes', 'no'])
    })

    print(df.loc[0:1, ["A", "B"]])
    print(df.iloc[0:1, 1:2])