echo "Cloning Custom Repo from $UPSTREAM_REPO "
git clone https://github.com/deepukumarpuri/unzip /unzip
fi
cd /unzip
pip3 install -U -r requirements.txt
echo "Starting TIGER Shroff....🔥"
python3 bot.py
