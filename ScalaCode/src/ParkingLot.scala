class ParkingLot( var rows: Int, var columns: Int ) {

  val lot: Array[Array[ParkingSpot]] = Array.ofDim[ParkingSpot](rows, columns)
  val spots: Int = rows * columns
  var filledSpots: Int = 0
  var counter = 0
  for( i <- 0 until rows; j <- 0 until columns ){
    lot(i)(j) = new ParkingSpot(-1, counter.toString)
    counter += 1
  }

  def update(): Unit = {
    for( row <- lot; spot <- row ){
      if( spot.filled ) {
        spot.checkFilled()
        if(!spot.filled)
          filledSpots -= 1
      }
      else if( !spot.filled ){
        if( spot.distance > 100 )
          spot.timer = 0
        else if( spot.timer == 0 )
          spot.timer = System.nanoTime()
        else {
          spot.checkFilled()
          if(spot.filled)
            filledSpots += 1
        }
      }
    }
  }

  def percentFilled(): Double = {
    ( filledSpots.asInstanceOf[Double] / spots.asInstanceOf[Double] ) * 100
  }

}
