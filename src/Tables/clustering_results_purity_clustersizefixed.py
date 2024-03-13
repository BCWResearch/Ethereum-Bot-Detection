from src.Datamodels.Table import Table
import pandas as pd

class Tab(Table):

    def __init__(self):
        # get name of this script
        script_name = __file__
        name, chapter, runs = script_name, "results", ["large"]
        super().__init__(name, chapter, runs)

    def set_outnames(self):
        self.outnames = [self.name]

    def create_tex_code(self):
        df = self.load_data()
        # in the multiindex replace "gmm" with "GMM"
        df.index = df.index.set_levels(df.index.levels[0].str.replace("gmm", "GMM"), level=0)

        df = df.unstack(level=-1)
        # flatten column name levels
        level0 = df.columns.get_level_values(0)
        level1 = df.columns.get_level_values(1)
        df.columns = [f"thead[[[{i} latexnewline {j} Clusters]]]" for i, j in zip(level0, level1)]

        df.index.names = ["Algorithm", "Imputation", "thead[[[Dimension. latexnewline Reduction]]]"]


        tex_string = df.to_latex(index=True)
        return tex_string


if __name__ == "__main__":
    prefix = "../.."
    v = Tab()
    v.prefix = prefix
    v.create_and_save()