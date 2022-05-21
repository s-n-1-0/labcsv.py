# %% import and read
from labcsv import read_csv,DefaultHeaderName as LHName
rlab = read_csv("tests/test.csv")

# %% test/get_column_values
#arg->list
print(rlab.get_column_values([LHName.TIME_COMMIT,
                            LHName.SENDER]))
print(rlab.get_column_values([LHName.SENDER_ID]))
#args->all LHName
for name in LHName:
    print(f"----{name.value}")
    print(rlab.get_column_values(name))


# %% test/get_meta
meta = rlab.get_meta()
print(meta["labjs_version"])
print(meta["language"])
print(meta["location"])
# %%
