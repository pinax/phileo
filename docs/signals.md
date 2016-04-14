Signals
=======

Both of these signals are sent from the `Like` model in the view that
processes the toggling of likes and unlikes.

likes.signals.object\_liked
---------------------------

This signal is sent immediately after the object is liked and provides
the single `kwarg` of `like` which is the instance of the `Like` object that
was created.

likes.signals.object\_unliked
-----------------------------

This signal is sent immediately after the object is unliked and provides
the single `kwarg` of `object` which is the objects that was just unliked.
