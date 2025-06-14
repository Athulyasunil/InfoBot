// app/page.tsx
'use client';

import { useState } from 'react';
import { Send, Loader2 } from 'lucide-react';

interface ImageInfo {
  image_url: string;
  title?: string;
  creator?: string;
  license?: string;
}

interface ChatMessage {
  id: string;
  query: string;
  summary: string;
  imageInfo?: ImageInfo;
  timestamp: Date;
}

interface ApiResponse {
  summary: string;
  image_info?: ImageInfo;
}

export default function Home() {
  const [query, setQuery] = useState('');
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim() || loading) return;

    const currentQuery = query.trim();
    setQuery('');
    setLoading(true);
    setError(null);

    try {
      const response = await fetch('/api/ask', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: currentQuery }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data: ApiResponse = await response.json();
      
      const newMessage: ChatMessage = {
        id: Date.now().toString(),
        query: currentQuery,
        summary: data.summary,
        imageInfo: data.image_info,
        timestamp: new Date(),
      };
      console.log('Summary:', newMessage.summary);
      console.log('Image Info:', newMessage.imageInfo);

      setMessages(prev => [...prev, newMessage]);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to get response');
    } finally {
      setLoading(false);
    }
  };

  const formatTime = (date: Date) => {
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-4xl mx-auto px-4 py-4">
          <h1 className="text-2xl font-bold text-gray-900">AI Research Chat</h1>
          <p className="text-gray-600 text-sm">Ask questions and get comprehensive answers with relevant images</p>
        </div>
      </header>

      {/* Chat Messages */}
      <main className="flex-1 max-w-4xl mx-auto w-full px-4 py-6">
        <div className="space-y-6">
          {messages.length === 0 && (
            <div className="text-center py-12">
              <div className="text-gray-400 text-lg mb-2">👋</div>
              <h2 className="text-xl font-semibold text-gray-700 mb-2">Welcome to AI Research Chat</h2>
              <p className="text-gray-500">Ask me anything and I'll provide a comprehensive summary with relevant images!</p>
            </div>
          )}

          {messages.map((message) => (
            <div key={message.id} className="bg-white rounded-lg shadow-sm border p-6">
              {/* User Query */}
              <div className="mb-4">
                <div className="flex items-center gap-2 mb-2">
                  <div className="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center">
                    <span className="text-white text-sm font-medium">You</span>
                  </div>
                  <span className="text-sm text-gray-500">{formatTime(message.timestamp)}</span>
                </div>
                <p className="text-gray-900 font-medium ml-10">{message.query}</p>
              </div>

              {/* AI Response */}
              <div className="ml-10 pl-4 border-l-2 border-gray-100">
                <div className="flex items-center gap-2 mb-3">
                  <div className="w-8 h-8 bg-green-500 rounded-full flex items-center justify-center">
                    <span className="text-white text-sm font-medium">AI</span>
                  </div>
                  <span className="text-sm font-medium text-gray-700">Summary</span>
                </div>
                
                <div className="prose prose-sm max-w-none">
                  <p className="text-gray-800 leading-relaxed whitespace-pre-wrap">{message.summary}</p>
                </div>

                {/* Image Display */}

                {message.imageInfo && (
                  <div className="mt-4 p-4 bg-gray-50 rounded-lg">
                    <div className="flex justify-start">
                      <img
                        src={message.imageInfo.image_url}
                        alt="Related"
                        className="min-w-[150px] max-w-[300px] max-h-[200px] object-contain rounded-lg shadow-sm"
                        loading="lazy"
                      />
                    </div>

                    {(message.imageInfo.title || message.imageInfo.creator) && (
                      <div className="mt-2 text-xs text-gray-600">
                        {message.imageInfo.title && (
                          <p className="font-medium">{message.imageInfo.title}</p>
                        )}
                        {message.imageInfo.creator && (
                          <p>by {message.imageInfo.creator}</p>
                        )}
                        {message.imageInfo.license && (
                          <p className="text-gray-500">License: {message.imageInfo.license}</p>
                        )}
                      </div>
                    )}
                  </div>
                )}
              </div>
            </div>
          ))}

          {/* Loading State */}
          {loading && (
            <div className="bg-white rounded-lg shadow-sm border p-6">
              <div className="flex items-center gap-3">
                <Loader2 className="w-5 h-5 animate-spin text-blue-500" />
                <span className="text-gray-600">Processing your query...</span>
              </div>
            </div>
          )}

          {/* Error State */}
          {error && (
            <div className="bg-red-50 border border-red-200 rounded-lg p-4">
              <p className="text-red-800">Error: {error}</p>
            </div>
          )}
        </div>
      </main>

      {/* Input Form */}
      <footer className="bg-white border-t shadow-sm">
        <div className="max-w-4xl mx-auto px-4 py-4">
          <form onSubmit={handleSubmit} className="flex gap-3">
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Ask me anything..."
              className="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              disabled={loading}
            />
            <button
              type="submit"
              disabled={loading || !query.trim()}
              className="px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center gap-2"
            >
              {loading ? (
                <Loader2 className="w-4 h-4 animate-spin" />
              ) : (
                <Send className="w-4 h-4" />
              )}
              Send
            </button>
          </form>
        </div>
      </footer>
    </div>
  );
}