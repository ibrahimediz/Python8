from tabula import read_pdf
import tabula
tabula.convert_into(r"D:\ibrahim_ediz\Ornekler\test\data\tabla_subsidios.pdf", "test_s.csv", output_format="csv")
df = read_pdf(r"D:\ibrahim_ediz\Ornekler\test\data\tabla_subsidios.pdf")
print()