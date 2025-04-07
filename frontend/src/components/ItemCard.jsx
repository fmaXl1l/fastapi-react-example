import { Link } from 'react-router-dom'

const ItemCard = ({ item }) => {
  return (
    <div className="card hover:shadow-lg transition-shadow">
      <h3 className="text-xl font-semibold mb-2">{item.title}</h3>
      <p className="text-gray-600 mb-4 line-clamp-2">{item.description || 'No description available'}</p>
      <div className="flex justify-between items-center">
        <span className="text-lg font-bold text-blue-600">${item.price.toFixed(2)}</span>
        <span className={`px-2 py-1 rounded-full text-xs font-semibold ${
          item.available ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
        }`}>
          {item.available ? 'Available' : 'Unavailable'}
        </span>
      </div>
      <div className="mt-4">
        <Link to={`/items/${item.id}`} className="btn btn-primary w-full text-center">
          View Details
        </Link>
      </div>
    </div>
  )
}

export default ItemCard
