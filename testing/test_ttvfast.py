import sys
sys.path.insert(0, '.')
import ttvfast
import numpy as np


def test_ttvfast():
    params = [
        0.000295994511,
        0.95573417954,
        0.00002878248,
        1.0917340278625494e+01,
        5.6159310042858110e-02,
        9.0921164935951211e+01,
        -1.1729336712101943e-18,
        1.8094838714599581e+02,
        -8.7093652691581923e+01,
        0.00061895914,
        2.2266898036209028e+01,
        5.6691301931178648e-02,
        8.7598285693573246e+01,
        4.6220554014026838e-01,
        1.6437004273382669e+00,
        -1.9584857031843157e+01]

    Time = -1045
    dt = 0.54
    Total = 1700
    n_plan = 2
    input_flag = 0
    n_events = 5000

    results = ttvfast.ttvfast(
        params, dt, Time, Total, n_plan, n_events, input_flag)
    python_rows = zip(*results)

    with open('TTVFast/c_version/output.txt') as infile:
        for i, (python_row, c_row) in enumerate(
                zip(python_rows, infile)):
            c_row = c_row.strip().split()
            vals = (int(c_row[0]),
                    int(c_row[1]),
                    float(c_row[2]),
                    float(c_row[3]),
                    float(c_row[4]))
            assert np.allclose(vals, python_row)

    assert i == 374
