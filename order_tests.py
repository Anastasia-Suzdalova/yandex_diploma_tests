import sender
import data

def test():
    resp = sender.create_order(data.order)
    assert resp.status_code == 201

    track = resp.json()["track"]
    resp = sender.get_order_by(track)
    assert resp.status_code == 200
