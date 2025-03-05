script_dir=$PWD

cd $script_dir
cd ..

parentdir=$PWD

cd $parentdir

if [ ! -d "venv" ]; then
    python -m venv venv
    venv/bin/pip install .
fi

source venv/bin/activate

python src/autozenith/__main__.py