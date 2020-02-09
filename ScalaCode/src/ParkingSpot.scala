class ParkingSpot( var ID: (Int, Int) ) {

  var filled = false

  def checkFilled( update: Boolean ): Unit = {
    filled = update
  }

}
