import functools
from visidata import vd, Progress

try:
    import tabulate
    for fmt in tabulate.tabulate_formats:
        def save_table(path, *sheets):
            import tabulate

            with path.open_text(mode='w') as fp:
                for vs in sheets:
                    fp.write(tabulate.tabulate(
                        vs.itervals(*vs.visibleCols, format=True),
                        headers=[ col.name for col in vs.visibleCols ],
                        tablefmt=fmt))

        setattr(vd, 'save_'+fmt, save_table)
except ModuleNotFoundError:
    pass
