class ParkingSpot( var distance: Int, var ID: String ) {

  var filled = false
  var timer: Long = 0

  def updateDistance( updated: Int ): Unit = {
    this.distance = updated
  }

  def checkFilled(): Unit = {
    val seconds = (System.nanoTime() - timer) / 1000000000
    if( this.distance <= 100 && seconds >= 30 )
      filled = true
    else
      filled = false
  }

}
