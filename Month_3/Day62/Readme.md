ML -- Pattern Recognition.

Linear Regression --
Find Relationship --> Predict unseen values.

Example - If a restaurant gets 1000 orders a day, how many delivery partners will w probably need?

Historical Data:
Orders	Delivery Partners
100	12
200	20
300	31
400	40
500	51

More orders --> More Delivery Partners

If someone asks : 750 orders?
We estimate.... ML Does the same thing.
This is Regression.

### So where does the line come from?

Imagine joining these points.

•

   •

      •

          •

              •

If I ask you:

Draw ONE line that best represents all these points.

You'll probably draw something like:

         /

      /

   /

/

That line is simply your summary of the relationship.
The computer is trying to draw the same "best" line.

### How does coputer decide:
Which line is the BEST line?

--- Error & Mean Squared Error[MSE]